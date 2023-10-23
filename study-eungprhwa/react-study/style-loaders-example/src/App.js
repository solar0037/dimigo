import logo from "./logo.svg";
// import './App.css';
// import './App.scss';
import styles from "./App.module.css";
// import Button from './components/Button';
import StyledButton from "./components/StyledButton";
import StyledButton2 from "./components/StyledButton2";
import styled from "styled-components";

const UpperCaseButton = (props) => (
  <button {...props} children={props.children.toUpperCase()} />
);

const MyButton = (props) => (
  <button {...props} children={`MyButton ${props.children}`}></button>
);

const StyledMyButton = styled(MyButton)`
  background: transparent;
  border-radius: 3px;
  border: 2px solid red;
  color: red;
  margin: 0 1em;
  padding: 0.25em 1em;
  font-size: 20px;
`;

const PrimaryStyledButton = styled(StyledButton)`
  background: blue;
  color: white;
`;

function App() {
  return (
    <div className={styles["App"]}>
      <header className={styles["header"]}>
        <img src={logo} className={styles["logo"]} alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        {/* <Button>Button</Button> */}
        <StyledButton>StyledButton</StyledButton>
        <StyledButton primary={true}>StyledButton</StyledButton>
        <PrimaryStyledButton>버튼</PrimaryStyledButton>
        <StyledButton as="a" href="/">
          버튼
        </StyledButton>
        <StyledButton as={UpperCaseButton}>button</StyledButton>
        <StyledButton2>h1</StyledButton2>
        <StyledMyButton>StyledMyButton</StyledMyButton>
        {/* <a
          className={styles["link"]}
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
    </div>
  );
}

export default App;
