/*
 * Copyright 2017 Ankur Yadav (ankurayadav@gmail.com)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * 		http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package dgraph

import "testing"

// BenchmarkDataLoad loads data to dgraph db.
func BenchmarkImportDataToDB(b *testing.B) {
	for i := 0; i < b.N; i++ {
		ImportDataToDB()
	}
}

// BenchmarkQueryFilmByDirector_WithNodeIDGiven finding movies and genre of movies directed by "Steven Spielberg"?
func BenchmarkQueryFilmByDirector_WithNodeIDGiven(b *testing.B) {
	runBench(0, b)
}

// BenchmarkQueryFilmByDirector_WithNameGiven finding movies and genre of movies directed by "Steven Spielberg"?
func BenchmarkQueryFilmByDirector_WithNameGiven(b *testing.B) {
	runBench(1, b)
}
