import logo from "./logo.svg";
import "./App.css";
// import Example1 from "./components/Example1";
// import Example2 from "./components/Example2";
// import Example3 from "./components/Example3";
// import Example4 from "./components/Example4";
import Example5 from "./components/Example5";

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <Example1 />
//         <Example2 />
//         <Example3 />
//         <Example4 />
//         <Example5 />
//       </header>
//     </div>
//   );
// }

// export default App;

import useWindowWidth from "./hooks/useWindowWidth";
import Example6 from "./components/Example6";
import Example7 from "./components/Example7";
import Example11 from "./components/Example11";
import Example12 from "./components/Example12";
import Example13 from "./components/Example13";

function App() {
  const width = useWindowWidth();
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {/* <Example1/>
<Example2/>
<Example3/>
<Example4/> */}
        {/* <Example5 />
        <Example6 />
        <Example7 /> */}
        <Example11 />
        <Example12 />
        <Example13 />
        {width}
      </header>
    </div>
  );
}
export default App;
