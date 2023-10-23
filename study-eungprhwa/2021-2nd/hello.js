// var i = 0;
// for (i=0; i<=10; i++) {
//     document.write("Hello World!");
//     document.write("<br>");
// }

function try1() {
    let num = 100;
    console.log("num", num);

    let num1 = 3.14;
    console.log("num1", num1);

    const a = "cocoa";
    console.log("[try1] before", a);

    if (true) {
        const a = "leaf";
        console.log("[if] before", a);

        console.log("[if] after", a);
    }
    console.log("[try1] after", a);
}

try1();
