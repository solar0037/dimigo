// let a = '3';

// // alert(a == 3);
// alert(a === String(3));

// let i = 0;

// document.write('<table border="1">');

// // for (let i=0; i<10; i++) {
// //     document.write('<tr><td>');
// //     document.write(i);
// //     document.write('</td></tr>');
// // }

// while (i < 20) {
//     document.write('<tr><td>');
//     document.write(i);
//     document.write('</td></tr>');
//     i++;
// }

// document.write('</table>');

// let i = 0;
// while (true) {
//     console.log(i);

//     if (i > 1000) {
//         break;
//     }

//     i++;
// }

// 에러메시지 처리 함수
function call_err(v1, v2) {
    let msg = 'Hello';
    let v3 = v2 || '00';
    if (v1) {
        msg += `, ${v1}님, 에러가 났습니다. (코드라인: ${v3})`
    }
    // document.write(msg);
    // confirm(msg);

    return msg;
}

let rtn_msg = call_err('관리자');
alert(rtn_msg);
