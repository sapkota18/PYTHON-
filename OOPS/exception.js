const Division = (a, b) => {
    try {
        if (b === 0) {
            throw new Error("Error: Division by zero is not allowed");
        } else {
            return a / b;  
        }
    } catch (err) {
        console.log(err.message);  
        return null;  
    }
};


console.log("Result:", Division(5, 6)); 
console.log("Result:", Division(4, 0));  
