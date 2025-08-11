from rest_framework import serializers
from .models import Professional
import re

def _clean_text(s: str) -> str:
    # remove espaços duplicados e trim
    return re.sub(r"\s+", " ", s or "").strip()

def _normalize_phone(s: str) -> str:
    # mantém somente dígitos e formata (XX) XXXXX-XXXX ou (XX) XXXX-XXXX
    digits = re.sub(r"\D", "", s or "")
    if len(digits) not in (10, 11):
        raise serializers.ValidationError("Contato deve ter 10 ou 11 dígitos (com DDD).")
    if len(digits) == 11:
        return f"({digits[0:2]}) {digits[2:7]}-{digits[7:11]}"
    return f"({digits[0:2]}) {digits[2:6]}-{digits[6:10]}"

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = ["id", "nome_social", "profissao", "endereco", "contato", "created_at", "updated_at"]

    # --- sanitização/normalização por campo ---
    def validate_nome_social(self, value):
        value = _clean_text(value)
        if len(value) < 3:
            raise serializers.ValidationError("Nome social deve ter ao menos 3 caracteres.")
        return value

    def validate_profissao(self, value):
        value = _clean_text(value)
        if len(value) < 2:
            raise serializers.ValidationError("Profissão deve ter ao menos 2 caracteres.")
        return value

    def validate_endereco(self, value):
        return _clean_text(value)

    def validate_contato(self, value):
        # normaliza e valida número
        return _normalize_phone(value)

    # --- garantimos que também limpe no update parcial ---
    def update(self, instance, validated_data):
        for field in ("nome_social", "profissao", "endereco"):
            if field in validated_data:
                validated_data[field] = _clean_text(validated_data[field])
        if "contato" in validated_data:
            validated_data["contato"] = _normalize_phone(validated_data["contato"])
        return super().update(instance, validated_data)
