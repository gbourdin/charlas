import './style.css';
import Print from './print.js';
  
const print = new Print();
const btn = document.getElementById('clear');
btn.onclick = () => {
  print.initialize();
}
