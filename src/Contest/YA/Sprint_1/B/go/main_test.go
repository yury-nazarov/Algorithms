package main

import "testing"

// go test -v
func TestIsWinInput1(t *testing.T){
	want := "FAIL"
	if got := IsWin("../data/input_1.txt"); got != want {
		t.Errorf("IsWin = %v, want = %v", got, want)
	}
}

func TestIsWinInput2(t *testing.T) {
	want := "WIN"
	if got := IsWin("../data/input_2.txt"); got != want {
		t.Errorf("IsWin = %v, want = %v", got, want)
	}
}

func TestIsWinInput3(t *testing.T) {
	want := "WIN"
	if got := IsWin("../data/input_2.txt"); got != want {
		t.Errorf("IsWin = %v, want = %v", got, want)
	}
}

// go test -bench .
func BenchmarkIsWinInput1(b *testing.B) {
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		IsWin("../data/input_1.txt")
	}
}

func BenchmarkIsWinInput2(b *testing.B) {
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		IsWin("../data/input_2.txt")
	}
}

func BenchmarkIsWinInput3(b *testing.B) {
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		IsWin("../data/input_3.txt")
	}
}


