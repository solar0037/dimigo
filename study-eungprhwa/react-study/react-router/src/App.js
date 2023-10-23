import './App.css';
import { BrowserRouter, Route, Switch, Link } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import Profile from './pages/Profile';
import NotFound from './pages/NotFound';
import NavLinks from './pages/Links';
import Login from './pages/Login';

function App() {
  return (
    <BrowserRouter>
      {/* <Switch> */}
        {/* <a href="/">Home으로 이동</a> */}
        {/* <Link to="/">Home으로 이동</Link> */}
        <NavLinks />
        <Route path="/" exact component={Home} />
        <Route path="/about" component={About} />
        <Route path="/profile/:id" component={Profile} />
        <Route path="/profile" component={Profile} />
        <Route path="/login" component={Login} />
        <Route component={NotFound} />
      {/* </Switch> */}
    </BrowserRouter>
  );
}

export default App;
