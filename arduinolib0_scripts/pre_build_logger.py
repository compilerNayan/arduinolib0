#!/usr/bin/env python3
"""
Professional logging utility for SpringBoot++ pre-build scripts.
Provides consistent, minimalist, and informative logging across all pre-build processes.
"""

import sys
from typing import Optional
from pathlib import Path


# Global state to track if banner has been printed
_banner_printed = False


def print_banner():
    """Print the SpringBoot++ ASCII art banner (only once per execution)."""
    global _banner_printed
    if _banner_printed:
        return
    
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     ███████╗██████╗ ██╗███╗   ██╗ ██████╗ ██████╗  ██████╗ ████████╗████████╗
║     ██╔════╝██╔══██╗██║████╗  ██║██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝
║     ███████╗██████╔╝██║██╔██╗ ██║██║   ██║██████╔╝██║   ██║   ██║      ██║   
║     ╚════██║██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══██╗██║   ██║   ██║      ██║   
║     ███████║██║     ██║██║ ╚████║╚██████╔╝██████╔╝╚██████╔╝   ██║      ██║   
║     ╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   
║                                                                              ║
║                              Pre-Build Processing                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
    print(banner)
    _banner_printed = True


def log_annotation_processed(annotation: str, file_path: str, details: Optional[str] = None):
    """
    Log when an annotation is successfully processed.
    
    Args:
        annotation: Name of the annotation (e.g., "@Serializable", "@Autowired")
        file_path: Path to the file where annotation was processed
        details: Optional additional details (e.g., class name, count)
    """
    file_name = Path(file_path).name
    message = f"  ✓ Processed {annotation}"
    if details:
        message += f" - {details}"
    message += f" in {file_name}"
    print(message)


def log_annotation_found(annotation: str, file_path: str, count: int = 1):
    """
    Log when annotations are found (but may already be processed).
    
    Args:
        annotation: Name of the annotation
        file_path: Path to the file
        count: Number of annotations found
    """
    file_name = Path(file_path).name
    if count > 1:
        print(f"  ℹ Found {count} {annotation} annotation(s) in {file_name}")
    else:
        print(f"  ℹ Found {annotation} annotation in {file_name}")


def log_processing_start(module_name: str):
    """
    Log the start of a processing module.
    
    Args:
        module_name: Name of the processing module (e.g., "Serialization", "Dependency Injection")
    """
    print(f"\n📦 Processing: {module_name}")


def log_summary(module_name: str, processed_count: int, total_count: int = None):
    """
    Log a summary of processing results.
    
    Args:
        module_name: Name of the module
        processed_count: Number of items processed
        total_count: Total number of items (optional)
    """
    if total_count is not None:
        print(f"  ✓ {module_name}: {processed_count}/{total_count} processed")
    else:
        print(f"  ✓ {module_name}: {processed_count} processed")


def log_error(message: str, file_path: Optional[str] = None):
    """
    Log an error message.
    
    Args:
        message: Error message
        file_path: Optional file path where error occurred
    """
    if file_path:
        file_name = Path(file_path).name
        print(f"  ✗ Error in {file_name}: {message}")
    else:
        print(f"  ✗ Error: {message}")


def log_warning(message: str, file_path: Optional[str] = None):
    """
    Log a warning message.
    
    Args:
        message: Warning message
        file_path: Optional file path where warning occurred
    """
    if file_path:
        file_name = Path(file_path).name
        print(f"  ⚠ Warning in {file_name}: {message}")
    else:
        print(f"  ⚠ Warning: {message}")


def log_info(message: str):
    """
    Log an informational message.
    
    Args:
        message: Informational message
    """
    print(f"  ℹ {message}")


def log_section_header(title: str):
    """
    Log a section header.
    
    Args:
        title: Section title
    """
    print(f"\n{'─' * 70}")
    print(f"  {title}")
    print(f"{'─' * 70}")


def log_completion():
    """Log completion of pre-build processing."""
    print(f"\n{'═' * 70}")
    print("  ✓ Pre-build processing completed successfully")
    print(f"{'═' * 70}\n")

