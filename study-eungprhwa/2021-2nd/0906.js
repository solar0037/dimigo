// function isAge(user) {
//     if (user.age < 20)
//         return true
//     else
//         return false
// }

// // 객체
// const Mike = {
//     name: "Mike",
//     age: 30,
//     alias: 'mycol',
//     fn_sample() {
//         if (this.age < 20)
//             return false
//         else
//             return true
//     }
// }

// // 객체
// const Jane = {
//     name: "Jane",
//     age: 19
// }

// // document.write(isAge(Mike))
// // document.write(isAge(Jane))

// // for (let aa in Mike) {
// //     document.write(`${aa}: ${Mike[aa]} <Br>`)
// // }

// document.write(Mike.fn_sample(19));

// let sayHello = function() {
//     document.write(`hello, i'm ${this.name}`)
// }
// let boy = {
//     name: 'Mike',
//     sayHello
// }
// let girl = {
//     name: 'Jane',
//     sayHello
// }

// girl.sayHello();
// boy.sayHello();

const gangwon = {
    resort: ["용평", "평창", "강촌", "강릉", "홍천"],
    print: function(delay=1000) {
        console.log(this.resort);
        setTimeout(() => {
            document.write(this.resort)
        }, delay)
    }
}
gangwon.print();