#!/usr/bin/node


exports.nbOccurences = function (list, searchElement) {
  let nbr = 0
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) nbr++
  }
  return nbr;
}
