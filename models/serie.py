from config.conexao import get_connection
class SerieModel:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, titulo, ano, categoria, sinopse, faixa_etaria, pais, idioma FROM series")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result