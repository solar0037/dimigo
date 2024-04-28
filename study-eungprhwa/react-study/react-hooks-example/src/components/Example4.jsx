import React from "react";

export default class Example1 extends React.Component {
  state = { count: 0 };

  render() {
    console.log("render(0)", this.state.count);
    const { count } = this.state;

    return (
      <div>
        <p>당신이 클릭한 횟수는 {count}번 입니다.</p>
        <button onClick={this.click}>Click me</button>
      </div>
    );
  }

  componentDidMount() {
    console.log("componentDidMount(1)", this.state.count);
  }

  componentDidUpdate() {
    console.log("componentDidUpdate(2)", this.state.count);
  }

  click = () => {
    this.setState({ count: this.state.count + 1 });
  };
}
