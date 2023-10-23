import React from "react";

export default function Example5() {
  const [count, setCount] = React.useState(0);
  // React.useEffect(() => {
  //   console.log("componentDidMount & componentDidUpdate", count);
  // }, [count]);

  React.useEffect(() => {
    console.log("componentDidMount", count);
    // componentWillUnMount 역할을 할때는
    // 새로운 함수를 리턴하도록 처리
    return () => {
      //cleanup
      //componentWillUnmount
    };
  }, []);
  React.useEffect(() => {
    console.log("componentDidMount & componentDidUpdate by count", count);
    return () => {
      //cleanup
      console.log("cleanup by count", count);
    };
  }, [count]);

  return (
    <div>
      <p>당신이 클릭한 횟수는 {count}번 입니다.</p>
      <button onClick={click}>Click me</button>
    </div>
  );

  function click() {
    setCount(count + 1);
  }
}
