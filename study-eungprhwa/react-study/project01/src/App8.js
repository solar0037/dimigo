import React, { Component } from 'react';

class App8 extends Component {
  constructor(props) {
    super(props);

    this.state = {
      loading: true,
      formData: 'no data',
    };

    this.handleData = this.handleData.bind(this);

    setTimeout(this.handleData, 4000);
  }

  handleData() {
    // const data = 'new data';
    // const { formData } = this.state;

    // this.setState({
    //   loading: false,
    //   formData: data,
    // });
    this.loading = false;
    this.formData = 'new new data';
    this.forceUpdate();
  }

  render() {
    return (
      <div>
        <span>로딩중상태: {String(this.loading)}</span>
        <span>결과: {this.formData}</span>
      </div>
    );
  }
}

export default App8;
