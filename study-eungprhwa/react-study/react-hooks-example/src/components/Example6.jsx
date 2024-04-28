import { useReducer } from "react";
//reducer : state를 변경하는 로직이 담겨있는 함수
const reducer = (state, action) => {
  //기존 state 가 action 과 만나서 새로운 newState를 생성
  if (action.type === "PLUS") {
    return {
      count: state.count + 1,
    };
  }
  return state;
};
//dispatch : action 객체를 넣어서 실행
// action : 객체이고 필수 프로퍼티로 type을 가진다.
export default function Example6() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  return (
    <div>
      <p>당신이 클릭한 횟수는 {state.count} 번 입니다. </p>
      <button onClick={click}>클릭!!!</button>
    </div>
  );
  function click() {
    dispatch({ type: "PLUS" });
  }
}
