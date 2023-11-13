#!/usr/bin/node
const sz = Math.floor(Number(process.argv[2]));
if (isNaN(sz)) {
	console.log('Missing size');
} else {
	for (let i = 0; i < sz; i++){
		let s = '';
		for (let j = 0; j < sz; j++) s += 'X';
		console.log(s);
	}
}
