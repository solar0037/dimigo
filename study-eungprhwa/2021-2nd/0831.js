// // 선언문
// function sayHello(v) {
//     return 'okok';
// }

// // 표현식
// let sayHello = function(v) {
//     return 'okok';
// }

// // 화살표함수
// let sayHello = v => 'okok' + v
//     // document.write("Hello " + v);
// //     'okok'
// // )

// alert(sayHello('사호준학생'));
// // sayHello('사호준학생');

// // let result = sayHello('사호준학생');

// // let sayHello = function(v) {
// //     document.write("Hello " + v);
// //     return 'ok';
// // }

// // alert(result);

// const add = (num1, num2) => num1 + num2

// document.write(add(10, 25));

const superman = {
    name1: '사호준',
    age: 18,
}

// superman.name2 = '학생';
// superman.name3 = '학생1';
// if ('name3' in superman == true) {
//     alert(superman.name3);
// } else {
//     alert('없습니다.');
// }

// delete superman.name3;
// if ('name3' in superman == true) {
//     alert(superman.name3);
// } else {
//     alert('없습니다.');
// }

// alert(Object.keys(superman).length);

for (let key in superman) {
    alert(`${key} - ${superman[key]}`);
}