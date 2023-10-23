import LoginButton from '../components/LoginButton';

export default function Login(props) {
  //   function login() {
  //     setTimeout(() => {
  //       props.history.push('/');
  //     }, 1000);
  //   }
  return (
    <div>
      <h2>로그인 페이지입니다.</h2>
      {/* <button onClick={login}>로그인하기</button> */}
      <LoginButton props={props} />
    </div>
  );
}
