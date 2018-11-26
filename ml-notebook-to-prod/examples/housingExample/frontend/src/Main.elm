module Main exposing (..)

import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Http
import Forms
import Json.Decode as Decode
import Json.Encode as Encode
import FormatNumber exposing (format)
import FormatNumber.Locales exposing (spanishLocale)
import Debug


main : Program Never Model Msg
main =
    Html.program
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        }



-- Model

type alias Model =
    { houseForm : Forms.Form
    , currentPrice: Maybe Float
    }


-- Superficie del terreno
-- Superficie Cubierta
-- Nro de Habitaciones
-- Cant de Baños
-- Año de construccion

formFields : List ( String, List Forms.FieldValidator )
formFields =
    [ ( "floorSize", validateFloat)
    , ( "landSize", validateFloat)
    , ( "rooms", validateInt )
    , ( "bathrooms", validateInt )
    , ( "years", validateInt )
    ]


init : ( Model, Cmd Msg )
init =
    ({ houseForm = Forms.initForm formFields, currentPrice = Nothing
    }, Cmd.none)


-- Field Validators

validateExistence : String -> Maybe String
validateExistence string =
    if String.length string > 0 then
        Nothing
    else
        Just "Requerido"

validateNumber : (String -> Result error value) -> String -> String -> Maybe String
validateNumber f msg m =
     let
        n = f m
    in
        case n of
            Ok value ->
                Nothing

            Err _ ->
                Just msg



validateFloat : List Forms.FieldValidator
validateFloat =
  [validateExistence, (validateNumber String.toFloat "Cantidad con punto flotante")]


validateInt : List Forms.FieldValidator
validateInt =
    [ validateExistence
    , (validateNumber String.toInt "Cantidad entera")
    ]

-- Update


type Msg
    = UpdateFormText String String
    | Submit
    | GotPrice (Result Http.Error Float)


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        UpdateFormText fieldName value ->
            ({ model
                | houseForm =
                    Forms.updateFormInput model.houseForm fieldName value
            }, Cmd.none)
        Submit ->
          (model, getHousePrice model.houseForm)
        GotPrice (Ok r) ->
          ({model | currentPrice = Just r}, Cmd.none)
        GotPrice (Err e) ->
          let
              _ = (Debug.log "error" e)
          in
            (model, Cmd.none)


-- View


myField : Forms.Form -> String -> String -> String -> Html Msg
myField form name label_ step_ =
    div [ class "form-group" ]
        [ label [ for name ] [ text label_ ]
        , input
            [ class "form-control"
            , id name
            , placeholder label_
            , step step_
            , type_ "int"
            , onInput (UpdateFormText name)
            ]
            []
        , small [ class "form-text text-muted" ]
            [ text (Forms.errorString form name) ]
        ]

submitButtonAttributes : Bool -> List (Html.Attribute Msg)
submitButtonAttributes validateStatus =
    if validateStatus then
        [ class "btn btn-primary", type_ "submit" ]
    else
        [ class "btn", type_ "submit" ]

submit : Forms.Form -> Html Msg
submit form =
    button
        (submitButtonAttributes (Forms.validateStatus form))
        [ text "Submit" ]

view : Model -> Html Msg
view model =
  let
      price = case model.currentPrice of
      Just a -> "$" ++ (format spanishLocale a)
      Nothing -> "Esperando para cotizar"
    in
       --
    div [ class "container" ]
        [ div [ class "row"] [
            div [ class "col-md-3"] [h2 [] [text price]],
            div [ class "col-md-9"] [
            Html.form [onSubmit Submit]
            [ myField model.houseForm "floorSize" "Superficie de terreno" "0.1"
            , myField model.houseForm "landSize" "Superficie Cubierta" "0.1"
            , myField model.houseForm "rooms" "Cantidad de ambientes" "1"
            , myField model.houseForm "bathrooms" "Cantidad de baños" "1"
            , myField model.houseForm "years" "Año de construccion" "1"
            , submit model.houseForm
            ]
          ]]
        ]


-- Subscriptions

getHousePrice : Forms.Form -> Cmd Msg
getHousePrice form =
    postHouse form
        |> Http.send GotPrice


postHouse: Forms.Form -> Http.Request Float
postHouse form=
    Http.request
        { method = "POST"
        , headers = []
        , url = "http://localhost:8080/api/v1.0/predict"
        , body = Http.jsonBody (newFormEncoder form)
        , expect = Http.expectJson getFormResponse
        , timeout = Nothing
        , withCredentials = False
        }


convInt form value =
  let
      f = Forms.formValue form value
      s = String.toInt f
  in
      case s of
        Ok a ->
          a
        Err _->
          0


convFloat form value =
  let
      f = Forms.formValue form value
      s = String.toFloat f
  in
      case s of
        Ok a -> a
        Err _ -> 0.0


newFormEncoder : Forms.Form -> Encode.Value
newFormEncoder form =
    Encode.object
        [ ( "Rooms", Encode.int (convInt form "rooms"))
        , ("Bathroom", Encode.int (convInt form "bathrooms"))
        , ("Landsize", Encode.float (convFloat form "landSize"))
        , ("BuildingArea", Encode.float (convFloat form "floorSize"))
        , ("YearBuilt", Encode.int (convInt form "years"))
        ]

getFormResponse  =
  Decode.field "value" Decode.float

subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none
