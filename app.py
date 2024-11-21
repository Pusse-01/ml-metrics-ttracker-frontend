# app.py

import streamlit as st
from api_client import (
    upload_dataset,
    list_datasets,
    preprocess_dataset,
    download_dataset,
    evaluate_metrics,
    get_previous_results,
    get_saved_metrics,
    save_metrics,
)


def main():
    st.title("ML Metrics Tracker")

    menu = ["Metrics", "Previous Results", "Datasets"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Datasets":
        st.header("Datasets Management")
        dataset_menu = ["Upload Dataset", "List Datasets", "Preprocess Dataset"]
        dataset_choice = st.selectbox("Action", dataset_menu)

        if dataset_choice == "Upload Dataset":
            st.subheader("Upload a New Dataset")
            dataset_name = st.text_input("Dataset Name")
            uploaded_file = st.file_uploader("Choose a zip file", type=["zip"])
            if st.button("Upload"):
                if uploaded_file is not None:
                    result = upload_dataset(uploaded_file, dataset_name)
                    st.success(
                        f"Dataset uploaded successfully. ID: {result.get('metadata_id')}"
                    )
                    st.json(result)
                else:
                    st.error("Please upload a zip file.")

        elif dataset_choice == "List Datasets":
            st.subheader("Available Datasets")
            datasets = list_datasets()
            if datasets:
                for dataset in datasets:
                    st.write(dataset)
                    # st.write(f"**ID**: {dataset['id']}")
                    st.write(f"**Name**: {dataset['name']}")
                    st.write(f"**Classes**: {', '.join(dataset.get('classes', []))}")
                    st.write("---")
            else:
                st.info("No datasets available.")

        elif dataset_choice == "Preprocess Dataset":
            st.subheader("Preprocess a Dataset")
            datasets = list_datasets()
            dataset_options = {dataset["name"]: dataset["id"] for dataset in datasets}
            selected_dataset_name = st.selectbox(
                "Select Dataset", list(dataset_options.keys())
            )
            dataset_id = dataset_options[selected_dataset_name]

            st.write("Preprocessing Options:")
            resize_width = st.number_input("Resize Width", min_value=1, value=224)
            resize_height = st.number_input("Resize Height", min_value=1, value=224)
            grayscale = st.checkbox("Convert to Grayscale")
            normalize = st.checkbox("Normalize")
            rotation = st.slider(
                "Rotation Degrees", min_value=0, max_value=360, value=0
            )
            horizontal_flip = st.checkbox("Horizontal Flip")
            vertical_flip = st.checkbox("Vertical Flip")
            brightness = st.slider(
                "Brightness", min_value=0.0, max_value=2.0, value=1.0
            )
            contrast = st.slider("Contrast", min_value=0.0, max_value=2.0, value=1.0)
            saturation = st.slider(
                "Saturation", min_value=0.0, max_value=2.0, value=1.0
            )
            hue = st.slider("Hue", min_value=-0.5, max_value=0.5, value=0.0)

            if st.button("Preprocess"):
                preprocessing_options = {
                    "dataset_name": selected_dataset_name,
                    "resize_width": resize_width,
                    "resize_height": resize_height,
                    "grayscale": grayscale,
                    "normalize": normalize,
                    "rotation": rotation,
                    "horizontal_flip": horizontal_flip,
                    "vertical_flip": vertical_flip,
                    "brightness": brightness,
                    "contrast": contrast,
                    "saturation": saturation,
                    "hue": hue,
                }
                result = preprocess_dataset(dataset_id, preprocessing_options)
                st.success("Dataset preprocessed successfully.")
                st.json(result)

    elif choice == "Metrics":
        st.header("Model Metrics Evaluation")
        datasets = list_datasets()
        dataset_options = {dataset["name"]: dataset["id"] for dataset in datasets}
        if datasets:
            selected_dataset_name = st.selectbox(
                "Select Dataset", list(dataset_options.keys())
            )
            dataset_id = dataset_options[selected_dataset_name]
            model_type = st.selectbox(
                "Select Model Type", ["swin", "vit", "deit"]
            )  # Update with actual models

            if st.button("Evaluate Metrics"):
                result = evaluate_metrics(dataset_id, model_type)
                st.success("Metrics evaluated successfully.")
                st.json(result)
                # Store the evaluated metrics in session state
                st.session_state["evaluated_metrics"] = {
                    "dataset_id": dataset_id,
                    "model_type": model_type,
                    "results": result.get("results"),
                }
            # Check if evaluated_metrics are in session state
            if "evaluated_metrics" in st.session_state:
                if st.button("Save Metrics"):
                    metrics_data = st.session_state["evaluated_metrics"]
                    try:
                        save_response = save_metrics(metrics_data)
                        st.success("Metrics saved successfully.")
                        st.write(f"Metrics ID: {save_response.get('metrics_id')}")

                        # Clear the evaluated metrics from session state after saving
                        del st.session_state["evaluated_metrics"]
                    except Exception as e:
                        st.error(f"Failed to save metrics: {str(e)}")
        else:
            st.info(
                "No datasets available. Please upload and preprocess a dataset first."
            )

    elif choice == "Previous Results":
        st.header("Previous Results")
        result = get_saved_metrics()
        if "metrics" in result:
            metrics_list = result["metrics"]
            for metrics in metrics_list:
                st.subheader(f"Dataset ID: {metrics['dataset_id']}")
                st.write(f"Model Type: {metrics['model_type']}")
                st.write(f"Evaluated At: {metrics['evaluated_at']}")
                st.json(metrics["results"])
                st.write("---")
        else:
            st.info("No previous results found.")


if __name__ == "__main__":
    main()
