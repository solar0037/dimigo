import styles from "./Button.module.css";
import React from "react";

// const Button = (props) => <button className={styles["button"]} {...props}></button>
class Button extends React.Component {
  state = {
    loading: false,
  };

  startLoading = () => {
    this.setState({
      loading: true,
    });
    setTimeout(() => {
      this.setState({
        loading: false,
      });
    }, 2000);
  };

  render() {
    return (
      <button
        onClick={this.startLoading}
        className={
          this.state.loading
            ? `${styles["button"]} ${styles["loading"]}`
            : styles["button"]
        }
        {...this.props}
      />
    );
  }
}

export default Button;
