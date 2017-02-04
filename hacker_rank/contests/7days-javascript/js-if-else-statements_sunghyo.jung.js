res = '';
if(marks > 90) {
    res = 'AA';
} else if(marks > 80) {
    res = 'AB';
} else if(marks > 70) {
    res = 'BB';
} else if(marks > 60) {
    res = 'BC';
} else if(marks > 50) {
    res = 'CC';
} else if(marks > 40) {
    res = 'CD';
} else if(marks > 30) {
    res = 'DD';
} else {
    res = 'FF'
}
console.log(res);