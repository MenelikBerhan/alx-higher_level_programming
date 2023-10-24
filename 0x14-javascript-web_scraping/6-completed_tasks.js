#!/usr/bin/node
/*
Script that computes the number of tasks completed by user id.
  The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
  Only prints users with completed task
*/
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const todoList = JSON.parse(body);
    const result = {};
    for (const todo of todoList) {
      if (todo.completed) {
        result[todo.userId] = result[todo.userId] ? result[todo.userId] + 1 : 1;
      }
    }
    console.log(result);
  }
});
