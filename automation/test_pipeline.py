import unittest
from pipeline import Pipeline

class PipelineTest(unittest.TestCase):
    def test_split_five_subjects(self):
        text = "Mục lục: 1과목 소프트웨어 설계 2과목 소프트웨어 개발\n" + "\n".join(f"### {i}과목 {name}\nbody-{i}" for i, name in enumerate([
            "소프트웨어 설계", "소프트웨어 개발", "데이터베이스 구축", "프로그래밍 언어 활용", "정보시스템 구축 관리"
        ], 1))
        parts = Pipeline.split_parts(text)
        self.assertEqual(5, len(parts))
        self.assertIn("body-5", parts["05_정보시스템_구축관리.md"])

    def test_clean_ocr_markup(self):
        self.assertEqual("a\n\nb", Pipeline.clean("<mark>a</mark><br>\n\n######\n\nb"))

    def test_align_translation_by_core_id_not_position(self):
        pipeline = Pipeline()
        source = "### 핵심 **002** 소프트웨어 공학\nsource"
        translation = "### **001** Vòng đời\nwrong\n\n### **002** Kỹ nghệ phần mềm\nright"
        self.assertIn("right", pipeline.aligned_translation(source, translation))
        self.assertNotIn("wrong", pipeline.aligned_translation(source, translation))

    def test_extract_output_text(self):
        data = {"output": [{"type": "message", "content": [{"type": "output_text", "text": "ok"}]}]}
        self.assertEqual("ok", Pipeline.output_text(data))

if __name__ == "__main__":
    unittest.main()
