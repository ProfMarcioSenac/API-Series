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

    @staticmethod
    def get_by_id(serie_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, titulo, ano, categoria, sinopse, faixa_etaria, pais, idioma FROM series WHERE id = %s", (serie_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_by_title(texto):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, titulo, ano, categoria, sinopse, faixa_etaria, pais, idioma FROM series WHERE titulo like %s", (f"%{texto}%",))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_by_category(texto):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, titulo, ano, categoria, sinopse, faixa_etaria, pais, idioma FROM series WHERE categoria like %s", (f"%{texto}%",))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result