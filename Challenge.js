/*Use a standard JavaScript template. In your main function create the array below:

var squad = ["Bob", "John", "Bob", "Kenn", "Bob", "Kevin", "John", "Kevin"];
Print how many times each name is present in the array.
*/

/*A method that doesn't require to type out every individual in the array.*/
var a = ["Bob", "John", "Bob", "Kenn", "Bob", "Kevin", "John", "Kevin"];      /*array of names*/
var squad1= a.forEach(function(value) {                             /*uses for each to go through each element*/
    count = 1;               /*count for elements*/
    if (a.indexOf(value) == a.lastIndexOf(value))        /*if the index of the first instance of the element match the
                                                          index of the final instance, the count will remain 1.*/
    {
        console.log(value+ " count: "+count);           /*prints results*/
    }

    else                                         /*otherwise a loop will start where duplicate elements are removed
                                                 from the array from right to left until indexOf matches last IndexOf.
                                                 Also the count will increment plus 1 for each iteration */
    {
        while(a.indexOf(value)!=a.lastIndexOf(value))
        {
            count++;
            a.splice(a.lastIndexOf(value),1);

        }
        console.log(value+ " count: "+count)
    }

});
