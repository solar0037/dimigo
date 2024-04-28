import React, { useState, useEffect } from "react";
export default function useWindowWidth() {
  // 훅 안에서 훅을 사용 가능
  const [width, setWidth] = useState(window.innerWidth);
  // 윈도우에 resize 이벤트를 연결해서 width 값을 setWidth 에 받은 값으로 변경처리.
  // resize 이벤트를 어딘가에 설정해줘야 함 --> Hook에서 제공하는 useEffect를 사용한다.
  const resize = () => {
    setWidth(window.innerWidth);
  };
  useEffect(() => {
    window.addEventListener("resize", resize);
    return () => {
      window.removeEventListener("resize", resize);
    };
  });
  return width;
}
