let a=prompt("What is value of 'a'?\n","");
let b=prompt("What is value of 'b'?\n","");
let c=prompt("What is value of 'c'?\n","");
let root_part=Math.sqrt(b*b-4.0*a*c);
let denom=2.0*a;
let root1=(-b +root_part)/denom;
let root2=(-b -root_part)/denom;
console.log("The first root is:",root1,"<br/>");
console.log("The first root is:",root2,"<br/>");

