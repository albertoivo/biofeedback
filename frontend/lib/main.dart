import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_better_camera/camera.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget{
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> with SingleTickerProviderStateMixin{

  bool _toggled = false; // toggle button value
  List<HrvValue> _data = List<HrvValue>(); // array to store the values
  CameraController _controller;
  double _alpha = 0.3; // factor for the mean value
  AnimationController _animationController;
  double _iconScale = 1;
  int _bpm = 0; // beats per minute
  int _fs = 30; // sampling frequency (fps)
  int _windowLen = 30 * 6; // window length to display - 6 seconds
  CameraImage _image; // store the last camera image
  double _avg; // store the average value during calculation
  DateTime _now; // store the now Datetime
  Timer _timer; // timer for image processing

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(),
    );
  }
}


class HrvValue {
  final DateTime time;
  final double value;

  HrvValue(this.time, this.value);
}
