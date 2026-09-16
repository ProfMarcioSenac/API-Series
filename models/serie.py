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

    @staticmethod
    def get_by_language(texto):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, titulo, ano, categoria, sinopse, faixa_etaria, pais, idioma FROM series WHERE idioma like %s", (f"%{texto}%",))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_by_country(texto):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, titulo, ano, categoria, sinopse, faixa_etaria, pais, idioma FROM series WHERE pais like %s", (f"%{texto}%",))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def insert(dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO series (titulo, ano, categoria, sinopse, faixa_etaria, pais, idioma) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (dados.get('titulo'), dados.get('ano'), dados.get('categoria'), dados.get('sinopse'), dados.get('faixa_etaria'), dados.get('pais'), dados.get('idioma'))
        cursor.execute(sql, valores)
        conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return last_id

    @staticmethod
    def update(serie_id, dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE series set titulo=%s, ano=%s, categoria=%s, sinopse=%s, faixa_etaria=%s, pais=%s, idioma=%s WHERE id=%s"
        valores = (dados.get('titulo'), dados.get('ano'), dados.get('categoria'), dados.get('sinopse'), dados.get('faixa_etaria'), dados.get('pais'), dados.get('idioma'), serie_id)
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount > 0

    @staticmethod
    def delete(serie_id):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM series WHERE id = %s"
        valores = (serie_id,)
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount > 0