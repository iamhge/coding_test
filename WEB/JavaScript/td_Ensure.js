function ensure(value) {
    // Your code goes here
    if (value === undefined) {
        Error();
    }
    else {
        return value;
    }
}
  
try {
    console.log(ensure());
} catch(err) {
    console.log(err);
}