var isAnagram = function (s, t) {
  if (s.length === t.length) {
    let str1 = s
      .toLocaleLowerCase()
      .split("")
      .sort((a, b) => (a < b ? 1 : -1));

    let str2 = t
      .toLocaleLowerCase()
      .split("")
      .sort((a, b) => (a < b ? 1 : -1));

    console.log(
      str2.sort((a, b) => a - b).join("") ===
        str1.sort((a, b) => a - b).join("")
    );
    return str2.join("") === str1.join("");
  } else {
    return false;
  }
};

isAnagram("anagram", "nagaram");
