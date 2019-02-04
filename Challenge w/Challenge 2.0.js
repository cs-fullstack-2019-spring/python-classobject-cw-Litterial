/*Challenge 2.0 without using forEach function*/
var a = ["Bob", "John", "Bob", "Kenn", "Bob", "Kevin", "John", "Kevin"];

for (i=0;i<a.length;i++)
{   sum=1;                                 /*since the sum is inside the for loop, the sum resets to one when it goes
                                            to the next element in the array*/
    if (a.indexOf(a[i])== a.lastIndexOf(a[i]))
    {
        console.log(a[i]+" count: " +sum);
    }
    else                                         /*More or less same code from Challenge 1.0*/
    {
        while(a.indexOf(a[i])!=a.lastIndexOf(a[i]))
        {
            sum++;
            a.splice(a.lastIndexOf(a[i]),1);


        }
        console.log(a[i]+" count: " +sum);               /*No undefined results since a function isn't used*/
    }
}
