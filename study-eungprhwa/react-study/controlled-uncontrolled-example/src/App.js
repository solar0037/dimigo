// import logo from "./logo.svg";
import "./App.css";
import ControlledComponent from "./components/ControlledComponent";
import UnControlledComponent from "./components/UnControlledComponent";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ControlledComponent></ControlledComponent>
        <UnControlledComponent></UnControlledComponent>
      </header>
    </div>
  );
}

export default App;
