import React, { Component } from 'react';

class App10 extends Component {
  state = {
    counter: 1,
  };

  constructor(props) {
    super(props);
    console.log('constructor');
  }

  componentDidMount() {
    console.log('componentDidMount');
  }

  handleClick = () => {
    this.setState({
      counter: this.state.counter + 1,
    });
  };

  render() {
    return (
      <div>
        <h1>안녕하세요 리액트</h1>
        <MyComponent value={this.state.counter} />
        <button onClick={this.handleClick} />
      </div>
    );
  }
}

class MyComponent extends Component {
  state = {
    value: 0,
  };

  static getDerivedStateFromProps(nextProps, prevState) {
    if (prevState.value !== nextProps.value) {
      return {
        value: nextProps.value,
      };
    }
    return null;
  }

  render() {
    return (
      <div>
        <p>props: {this.props.value}</p>
        <p>state: {this.state.value}</p>
      </div>
    );
  }
}

export default App10;
