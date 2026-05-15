class AIFormatter:
    @staticmethod
    def format_for_ai(target, dork_results, social_results):
        prompt = f"--- OSINT ANALYSIS REPORT: {target} ---\n\n"
        
        prompt += "DOCUMENTS FOUND IN GOV/AC DOMAINS:\n"
        for res in dork_results:
            prompt += f"- {res['title']} ({res['link']})\n"
            
        prompt += "\nSOCIAL MEDIA FOOTPRINT:\n"
        for soc in social_results:
            prompt += f"- {soc['platform']}: {soc['link']}\n"
            
        prompt += "\nINSTRUCTION: Analisis data di atas. Identifikasi potensi kebocoran NIK, alamat, atau jabatan subjek. Berikan profil risiko digital dalam bahasa Indonesia."
        return prompt
