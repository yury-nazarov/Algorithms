package main

import "testing"

func TestRun_1(t *testing.T) {
	inputString := "aaabbbcccccaaaaa"
	expectString := "a8b3c5"
	if outputString := Counter(inputString); outputString != expectString {
		t.Errorf("outputString: %s, expectString: %s.", outputString, expectString)
	}
}

func TestRun_2(t *testing.T) {
	inputString := "zzzzcccUUUuu"
	expectString := "U3c3u2z4"
	if outputString := Counter(inputString); outputString != expectString {
		t.Errorf("outputString: %s, expectString: %s.", outputString, expectString)
	}
}

func TestRun_3(t *testing.T) {
	inputString := "aaabbbccccc"
	expectString := "a3b3c5"
	if outputString := Counter(inputString); outputString != expectString {
		t.Errorf("outputString: %s, expectString: %s.", outputString, expectString)
	}
}

func TestRun_4(t *testing.T) {
	inputString := "ЯЯЯБББддд"
	expectString := "Б3Я3д3"
	if outputString := Counter(inputString); outputString != expectString {
		t.Errorf("outputString: %s, expectString: %s.", outputString, expectString)
	}
}
