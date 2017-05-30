import { Component, OnInit } from '@angular/core';
import * as io from 'socket.io-client';

@Component({
  selector: 'app-digest',
  templateUrl: './digest.component.html',
  styleUrls: ['./digest.component.css']
})
export class DigestComponent implements OnInit {

  socket = io('http://192.168.0.102:8080');

  constructor() { }

  ngOnInit() {
    this.socket.on('connect', function() {
      console.log('Connected');
    });

    this.socket.on('my_response', function (msg) {
      console.log(msg);
  });

 }
}
