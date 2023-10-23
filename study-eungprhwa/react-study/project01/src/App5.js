import React, { Component } from 'react';
import PropTypes from 'prop-types';

class App5 extends Component {
  render() {
    return <div>{typeof this.props.boolValue}</div>;
  }
}

App5.propTypes = {
  value: PropTypes.bool,
};

export default App5;
