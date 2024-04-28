import { useState } from "react";
function sum(persons) {
  console.log("sum...");
  return persons.map((person) => person.age).reduce((l, r) => l + r, 0); //0은초기값
}
export default function Example7() {
  const [value, setValue] = useState("");
  const [persons] = useState([
    { name: "Mark", age: 39 },
    { name: "Jane", age: 28 },
  ]);
  const count = sum(persons);
  return (
    <div>
      <input value={value} onChange={change} />
      <p>{count}</p>
    </div>
  );
  function change(e) {
    setValue(e.target.value);
  }
}
