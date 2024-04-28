import React, { Component } from 'react';
// import logo from './logo.svg';
// import Header from './Header';
// import Nav from './Nav';
// import Article from './Article';
// import App5 from './App5.js';
import App8 from './App8.js';
import './App.css';

class App extends Component {
  render() {
    return (
      <div>
        {/* <Header korean="한글" english="영어"></Header>
        <Nav></Nav>
        <Article></Article> */}
        <App8>
          <div>
            <span>자식 노드</span>
          </div>
        </App8>
      </div>
    );
  }
}

export default App;
