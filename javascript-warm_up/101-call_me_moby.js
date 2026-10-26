#!/usr/bin/node

function callMeMoby (x, theFunction) {
  for (let time = 1; time <= x; time++) {
    theFunction();
  }
}

exports.callMeMoby = callMeMoby;
