


package neo4j


import "testing"

// BenchmarkDataLoad loads data to neo4j db.
func BenchmarkImportDataToDB(b *testing.B) {
	for i := 0; i < b.N; i++ {
		ImportDataToDB()
	}
}

// BenchmarkQueryFilmByDirector finding movies and genre of movies directed by "Steven Spielberg"?
func BenchmarkQueryFilmByDirector(b *testing.B) {
	runBench(0, b)
}
