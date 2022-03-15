function test2(num1, num2) {
  const N = Number(num1);
  const M = Number(num2);
  var result = [];
  const output = [];
  const visited = new Array(N).fill(false);

  function dfs(count) {
    if (count === M) {
      result.push(parseInt(output.join("")));
      return;
    }
    for (let i = 0; i < N; i++) {
      if (visited[i] === true) continue;
      visited[i] = true;
      output.push(i + 1);
      dfs(count + 1);
      output.pop();
      visited[i] = false;
    }
  }

  dfs(0);
  return result;
}

const output1 = test2(2, 1);
console.log(output1); // —> [1, 2]
const output2 = test2(3, 2);
console.log(output2); // —> [12, 13, 21, 23, 31, 32]
const output3 = test2(3, 3);
console.log(output3); // —> [123, 132, 213, 231, 312, 321]
