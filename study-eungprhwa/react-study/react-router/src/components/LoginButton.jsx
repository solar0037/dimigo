import { withRouter } from "react-router";

export default withRouter(function LoginButton(props) {
  function login() {
    setTimeout(() => {
      props.history.push('/');
    }, 1000);
  }
  return <button onClick={login}>로그인하기</button>;
});
