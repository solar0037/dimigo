# prototype-shop

- 2419 사호준
- CASE 2. 수업시간에 실습한 Prototype-shop 예제 코드 기반으로 업그레이드 제출 (zip 압축)

## 프로젝트 설명

- /: 상품 선택 페이지
- /checkout: 결제 페이지
- /*: Not Found 처리
- React Router를 이용하여 상품 선택 -> 결제로 이어지는 페이지간 이동을 구현해 보았습니다. `Home` 페이지에서 Checkout 버튼을 누르면 `useNavigate()` 훅을 이용하여 선택한 상품과 가격을 `Checkout` 페이지에 `state`로 넘겨줍니다. `Checkout` 페이지에서는 `location.state`에 담긴 값을 통해 상품 정보를 읽어 옵니다. Pay 버튼을 누르면 메시지를 출력하고 다시 상품 선택 페이지로 이동합니다.
- 상품 선택 페이지를 거치지 않고 /checkout을 요청하면 결제 화면 대신에 Wrong Request 화면을 출력합니다.
- 여러 페이지를 사용함에 따라, `Home` 페이지의 코드와 같이 묶여 있던 Context API를 `App.js`에서 React Router가 담당하게 하고 `Home.jsx`, `Checkout.jsx` 파일은 순수하게 컴포넌트 정의에만 사용되게 하였습니다.
- 교안에 나와 있는 버전 5와 달리 React Router 버전 6에 맞추어 각 `Route`를 `Routes`로 감쌌습니다.
- `Checkout`, `NotFound` 페이지의 CSS를 일부 수정했습니다.
- `Checkout` 페이지에서는 선택한 상품을 변경할 수 없게 설정했습니다.
