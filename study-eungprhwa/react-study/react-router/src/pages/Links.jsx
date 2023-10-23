import { NavLink } from 'react-router-dom';

function fnClick() {
  document.location.href = '/';
}

const activeStyle = {
  fontWeight: 'bold',
  color: 'green',
};

export default function Links() {
  return (
    <ul>
      <li>
        <NavLink to="/" exact activeStyle={activeStyle}>
          Home으로 이동
        </NavLink>
      </li>
      <li>
        <NavLink to="/profile" activeStyle={activeStyle}>
          Profile으로 이동
        </NavLink>
      </li>
      <li>
        <NavLink to="/profile/1" activeStyle={activeStyle}>
          Profile/1으로 이동
        </NavLink>
      </li>
      <li>
        <NavLink to="/about" activeStyle={activeStyle}>
          About으로 이동
        </NavLink>
      </li>
      <li>
        <NavLink to="/about?name=solar" activeStyle={activeStyle}>
          About?name=solar으로 이동
        </NavLink>
      </li>
      <li>
        <span onClick={fnClick}>JS 라우팅</span>
      </li>
    </ul>
  );
};
