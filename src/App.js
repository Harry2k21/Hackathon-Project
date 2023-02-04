import React from 'react';
import './App.css';
import Dino  from './assets/dino.png';

function App() {
  return (
    <div className="App">
      <h1>Jerry is hungry, feed him an image. </h1>
      <img src={Dino} alt="dino" />
      <div class="Logo"></div>
      {/* <Dino/> */}
      
      <button>Upload Image</button>
    </div>
  );
}

export default App;
