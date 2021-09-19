package main

import "testing"

func TestRun_1(t *testing.T) {
	want := -183
	if got := Run("../data/input_1.txt"); got != want {
		t.Errorf("Run() = %d, want %d", got, want)
	}
}

func TestRun_2(t *testing.T) {
	want := 40
	if got := Run("../data/input_2.txt"); got != want {
		t.Errorf("Run() = %d, want = %d", got, want)
	}
}

// go test -bench .
// Название, кол-во выполнений, время в наносекундах на операцию
// -benchmem - сколько было выделено байт за операцию (2/op), а также сколько раз за операцию выделялась память (allocs/op).
func BenchmarkRun100(b *testing.B) {
	b.ReportAllocs()
	for i := 0; i < b.N; i++ {
		Run("../data/input_1.txt")
	}
}

func BenchmarkRun2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_ = Run("../data/input_2.txt")
	}
}