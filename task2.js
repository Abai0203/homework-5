let score = 85;

if (score < 0 || score > 100) {
  console.log("Ошибка ввода");
} else if (score >= 90) {
  console.log("5");
} else if (score >= 75) {
  console.log("4");
} else if (score >= 60) {
  console.log("3");
} else {
  console.log("2");
}