/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {
    if (functions.length === 0) return x => x;
    return function (x) {
        let val = x;
        // Loops from the end to the beginning of the `functions` array
        for (let i = functions.length - 1; i >= 0; i--) {
            // Application of the current fn to val
            val = functions[i](val);
        }
        return val;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */